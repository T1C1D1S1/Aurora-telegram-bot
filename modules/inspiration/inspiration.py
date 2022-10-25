import inspirobot

INSPIRATION_HANDLER = inspirobot.flow()


def get_inspiration_text() -> str:
    INSPIRATION_HANDLER.fetch()
    fetched_quote = INSPIRATION_HANDLER.next()
    return fetched_quote.quote


def get_inspiration_image_url() -> str:
    image = inspirobot.generate()
    return image.url
