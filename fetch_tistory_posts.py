import feedparser

def fetch_recent_posts(feed_url, count=5):
    feed = feedparser.parse(feed_url)
    posts = []
    for entry in feed.entries[:count]:
        title = entry.title
        link = entry.link
        published_date = datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d')
        posts.append(f"- [{title}]({link}) ({published_date})")
    return "\n".join(posts)

def update_readme(file_path, new_content):
    with open(file_path, 'r') as file:
        readme_content = file.read()

    marker = "<!-- TISTORY:START -->"
    end_marker = "<!-- TISTORY:END -->"
    start_index = readme_content.find(marker) + len(marker)
    end_index = readme_content.find(end_marker)

    updated_content = readme_content[:start_index] + "\n" + new_content + "\n" + readme_content[end_index:]

    with open(file_path, 'w') as file:
        file.write(updated_content)

if __name__ == "__main__":
    rss_feed_url = "https://dev-jeongmin.tistory.com/rss"
    readme_file_path = "README.md"

    recent_posts = fetch_recent_posts(rss_feed_url)
    update_readme(readme_file_path, recent_posts)
