addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  const url = new URL(request.url);
  const path = url.pathname;

  // 处理 OPTIONS 请求（CORS 预检）
  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: getCorsHeaders() });
  }

  // 处理 GET 请求到 /api/chat
  if (request.method === 'GET' && path === '/api/chat') {
    const data = url.searchParams.get('data');
    
    if (!data) {
      return new Response(JSON.stringify({ error: '缺少参数 data' }), {
        status: 400,
        headers: { ...getCorsHeaders(), 'Content-Type': 'application/json' }
      });
    }

    const requestBody = {
      bot_id: '7641970700890882089',
      user_id: '123123***',
      stream: true,
      auto_save_history: true,
      additional_messages: [
        { role: 'user', content: data, content_type: 'text' }
      ]
    };

    try {
      const response = await fetch('https://api.coze.cn/v3/chat', {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer pat_xxx',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
      });

      const { readable, writable } = new TransformStream();
      response.body.pipeTo(writable);

      return new Response(readable, {
        headers: {
          ...getCorsHeaders(),
          'Content-Type': response.headers.get('Content-Type') || 'text/event-stream',
          'Transfer-Encoding': 'chunked'
        }
      });

    } catch (error) {
      return new Response(JSON.stringify({ error: error.message }), {
        status: 500,
        headers: { ...getCorsHeaders(), 'Content-Type': 'application/json' }
      });
    }
  }

  // 处理根路径请求
  if (path === '/' || path === '') {
    return new Response(`
      <!DOCTYPE html>
      <html>
      <head><title>Coze Proxy Worker</title></head>
      <body>
        <h1>Coze Proxy Worker 运行中</h1>
        <p>使用方法: GET /api/chat?data=消息内容</p>
      </body>
      </html>
    `, {
      headers: { 'Content-Type': 'text/html' }
    });
  }

  // 默认返回 404
  return new Response('Not Found', { status: 404 });
}

function getCorsHeaders() {
  return {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Access-Control-Max-Age': '86400'
  };
}
