import asyncio
import httpx

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = "YOUR_PERSONAL_ACCESS_TOKEN"
OWNER = "octocat"
REPO = "Hello-World"
BRANCH = "main"

MAX_CONCURRENT_FETCHES = 5  # adjust concurrency limit

async def fetch_file_content(client, file_path, semaphore):
    async with semaphore:
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO}/contents/{file_path}"
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        }
        params = {"ref": BRANCH}
        try:
            resp = await client.get(url, headers=headers, params=params)
            resp.raise_for_status()
            data = resp.json()
            print(f"[+] {file_path}: {data.get('size', 0)} bytes")
        except httpx.HTTPStatusError as e:
            print(f"[!] Error fetching {file_path}: {e}")

async def main():
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_FETCHES)
    async with httpx.AsyncClient() as client:
        # Fetch the list of files in the root directory
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO}/contents/"
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        }
        params = {"ref": BRANCH}
        resp = await client.get(url, headers=headers, params=params)
        resp.raise_for_status()
        items = resp.json()

        # Collect only files
        file_items = [item for item in items if item["type"] == "file"]
        print(f"Found {len(file_items)} files at repo root.")

        tasks = [fetch_file_content(client, item["path"], semaphore) for item in file_items]

        # Run tasks concurrently with bounded parallelism
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
