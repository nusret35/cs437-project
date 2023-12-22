import feedparser
import xml.etree.ElementTree as ET
from urllib.parse import quote



def news_feed_html():
    feed = feedparser.parse('https://www.ekonomidunya.com/rss_ekonomi_1.xml')
    subject = 'Ekonomi'
    main_news_item = feed.entries[0]
    title = main_news_item.title
    length = len(main_news_item.title)
    source_url = 'google.com'
    description = main_news_item.description[length+1:]
    image_src = main_news_item.links[0]['href']
    date = main_news_item.published
    href = f"single.html?title={quote(title)}&description={quote(description)}&image_src={quote(image_src)}&source_url={quote(source_url)}&date={quote(date)}&subject={quote(subject)}"
    main_html_content = f"""
    <div class="position-relative overflow-hidden" style="height: 500px;">
        <img class="img-fluid h-100" src="{image_src}" style="object-fit: cover;">
        <div class="overlay">
            <div class="mb-2">
                <a class="badge badge-danger text-uppercase font-weight-semi-bold p-2 mr-2">{subject}</a>
                <a class="text-white">{date}</a>
            </div>
            <a class="h2 m-0 text-white text-uppercase font-weight-bold" href={f"single.html?title={quote(title)}&description={quote(description)}&image_src={quote(href)}&source_url={quote('google.com')}&date={quote(date)}&subject={quote(subject)}"}>{title}</a>
        </div>
    </div>
    """
    secondary_html_content = ""
    remaining_html_content = ""
    print('printing news:')
    for item in feed.entries[1:5]:
        title = item.title
        length = len(item.title)
        source_url = 'google.com'
        description = item.description[length+1:]
        image_src = item.links[0]['href']
        date = item.published
        href = f"single.html?title={quote(title)}&description={quote(description)}&image_src={quote(image_src)}&source_url={quote(source_url)}&date={quote(date)}&subject={quote(subject)}"
        secondary_html_content += f"""
            <div class="col-md-6 px-0">
                <div class="position-relative overflow-hidden" style="height: 250px;">
                    <img class="img-fluid w-100 h-100" src={image_src} style="object-fit: cover;">
                    <div class="overlay">
                        <div class="mb-2">
                            <a class="badge badge-danger text-uppercase font-weight-semi-bold p-2 mr-2"
                                href="">{subject}</a>
                            <a class="text-white" href=""><small>{date}</small></a>
                        </div>
                        <a class="h6 m-0 text-white text-uppercase font-weight-semi-bold" href={href}>{title}</a>
                    </div>
                </div>
            </div>
        """

    for item in feed.entries[5:]:
        title = item.title
        length = len(item.title)
        source_url = 'google.com'
        description = item.description[length+1:]
        image_src = item.links[0]['href']
        date = item.published
        href = f"single.html?title={quote(title)}&description={quote(description)}&image_src={quote(image_src)}&source_url={quote(source_url)}&date={quote(date)}&subject={quote(subject)}"
        remaining_html_content += f"""
        <div class="position-relative overflow-hidden" style="height: 500px;">
            <img class="img-fluid h-100" src="{image_src}" style="object-fit: cover;">
            <div class="overlay">
                <div class="mb-2">
                    <a class="badge badge-danger text-uppercase font-weight-semi-bold p-2 mr-2">{subject}</a>
                    <a class="text-white">{date}</a>
                </div>
                <a class="h2 m-0 text-white text-uppercase font-weight-bold" href={href}>{title}</a>
            </div>
        </div>
        """

    return main_html_content, secondary_html_content, remaining_html_content

news_feed_html()