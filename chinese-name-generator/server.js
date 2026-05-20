const https = require('https');
const http = require('http');
const fs = require('fs');
const path = require('path');

const API_KEY = 'sk-82cbe5465ad04868b8a1689be50cf55e';
const API_HOST = 'api.deepseek.com';
const API_PATH = '/chat/completions';

const server = http.createServer((req, res) => {
    console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
    
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    if (req.method === 'OPTIONS') {
        res.writeHead(200);
        res.end();
        return;
    }

    if (req.method === 'POST' && req.url === '/api/generate-name') {
        let body = '';
        req.on('data', (chunk) => {
            body += chunk;
        });

        req.on('end', async () => {
            try {
                console.log(`[DEBUG] Request body: ${body}`);
                const data = JSON.parse(body);
                const englishName = data.name;
                console.log(`[INFO] Generating name for: ${englishName}`);

                const prompt = `
你是一位精通中英文名字文化的起名大师。请为英文名 "${englishName}" 生成3个有趣、有中国文化特色的中文名字。

要求：
1. 理解英文名字的含义和发音，巧妙转化为中文名字
2. 每个名字都要有中国文化元素（如诗词、典故、成语、神话等）
3. 加入幽默和网络梗元素，让名字更有趣
4. 每个名字提供中英文寓意解释

输出格式（JSON）：
{
    "names": [
        {
            "chinese": "中文名",
            "meaning_cn": "中文寓意解释",
            "meaning_en": "English meaning explanation",
            "cultural_note": "文化背景说明（可选）"
        }
    ]
}
`.trim();

                console.log('[INFO] Calling DeepSeek API...');
                const response = await callDeepSeekAPI(prompt);
                console.log(`[DEBUG] API response received, length: ${response.length}`);
                
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(response);
                console.log('[INFO] Response sent successfully');
            } catch (error) {
                console.error('[ERROR]', error);
                res.writeHead(500, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: '生成名字失败，请重试: ' + error.message }));
            }
        });
        return;
    }

    let filePath = '.' + req.url;
    if (filePath === './') {
        filePath = './index.html';
    }

    const extname = path.extname(filePath);
    const contentType = getContentType(extname);

    fs.readFile(filePath, (error, content) => {
        if (error) {
            if (error.code === 'ENOENT') {
                res.writeHead(404);
                res.end('File not found');
            } else {
                res.writeHead(500);
                res.end('Server error: ' + error.code);
            }
        } else {
            res.writeHead(200, { 'Content-Type': contentType });
            res.end(content, 'utf-8');
        }
    });
});

function callDeepSeekAPI(prompt) {
    return new Promise((resolve, reject) => {
        const requestData = JSON.stringify({
            model: 'deepseek-v4-flash',
            messages: [
                { 
                    role: 'system', 
                    content: '你是一位精通中英文名字文化的起名大师，擅长将英文名转化为有趣的中文名。请严格按照JSON格式输出。' 
                },
                { 
                    role: 'user', 
                    content: prompt 
                }
            ],
            stream: false
        });

        console.log(`[DEBUG] API request data length: ${requestData.length}`);

        const options = {
            hostname: API_HOST,
            path: API_PATH,
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${API_KEY}`,
                'Content-Length': Buffer.byteLength(requestData)
            },
            timeout: 60000
        };

        console.log('[DEBUG] Sending HTTPS request to DeepSeek API...');
        const req = https.request(options, (res) => {
            console.log(`[DEBUG] API response status: ${res.statusCode}`);
            
            let body = '';
            res.on('data', (chunk) => {
                body += chunk;
            });
            res.on('end', () => {
                console.log(`[DEBUG] API response body length: ${body.length}`);
                
                try {
                    const result = JSON.parse(body);
                    console.log(`[DEBUG] API response parsed`);
                    
                    if (result.choices && result.choices[0] && result.choices[0].message) {
                        const content = result.choices[0].message.content;
                        console.log(`[DEBUG] Extracted content length: ${content.length}`);
                        resolve(content);
                    } else if (result.error) {
                        console.error('[ERROR] API error:', result.error);
                        reject(new Error('API Error: ' + (result.error.message || JSON.stringify(result.error))));
                    } else {
                        console.error('[ERROR] Unexpected API response');
                        reject(new Error('Unexpected API response'));
                    }
                } catch (error) {
                    console.error('[ERROR] JSON parse error:', error);
                    console.error('[DEBUG] Raw body:', body.substring(0, 500));
                    reject(new Error('JSON parse error: ' + error.message));
                }
            });
        });

        req.on('timeout', () => {
            console.error('[ERROR] Request timeout');
            req.destroy();
            reject(new Error('Request timeout (60s)'));
        });

        req.on('error', (error) => {
            console.error('[ERROR] Request error:', error);
            reject(error);
        });

        req.write(requestData);
        req.end();
    });
}

function getContentType(extname) {
    const contentTypes = {
        '.html': 'text/html',
        '.js': 'text/javascript',
        '.css': 'text/css',
        '.json': 'application/json',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.gif': 'image/gif',
        '.svg': 'image/svg+xml',
        '.ico': 'image/x-icon'
    };
    return contentTypes[extname] || 'application/octet-stream';
}

const PORT = process.env.PORT || 3001;
server.listen(PORT, () => {
    console.log(`[INFO] Server running at http://localhost:${PORT}/`);
    console.log(`[INFO] Using DeepSeek API at ${API_HOST}`);
});

server.on('error', (err) => {
    console.error('[FATAL] Server error:', err);
});