import pytest
@pytest.mark.asyncio
async def test_convert(get_client):
    with open('file.txt','r+') as file:
        file_content = file.read()
    response = await get_client.post('/api/v1/pdf',files={'file.txt':file_content})
    assert response.status_code == 422