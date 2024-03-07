test_client = app.test_client()
async with test_client.websocket('/ws/') as test_websocket:
    await test_websocket.send(data)
    result = await test_websocket.receive()

    