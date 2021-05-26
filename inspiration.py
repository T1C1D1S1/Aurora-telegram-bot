import inspirobot

INSPIRATION_HANDLER = inspirobot.flow()


def inspiration_text():
    INSPIRATION_HANDLER.fetch()
    fetched_quote = INSPIRATION_HANDLER.next()
    return fetched_quote.quote


def insperation_image_url():
    image = inspirobot.generate()
    return image.url
