import httpx
from fastmcp import FastMCP

mcp = FastMCP("Safemap_Cloud_MCP")
API_KEY = "NBHJMZF7-NBHJ-NBHJ-NBHJ-NBHJMZF7VO"
BASE_URL = "https://www.safemap.go.kr/openapi2"

@mcp.tool()
async def get_safemap_data(
    service_id: str,
    page_no: int = 1,
    num_of_rows: int = 10,
    data_type: str = "JSON"
) -> str:
    """
    행정안전부 생활안전지도 Open API 데이터를 조회합니다.
    - service_id: API 서비스 ID (예: 범죄주의구간 'IF_0083', 안전비상벨 'IF_0045')
    """
    url = f"{BASE_URL}/{service_id}"
    params = {
        "serviceKey": API_KEY,
        "pageNo": str(page_no),
        "numOfRows": str(num_of_rows),
        "type": data_type
    }
    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(url, params=params)
        return response.text

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
