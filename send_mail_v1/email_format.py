msg_format = """
Hello {name},

Hope you're doing well. Thank you for joining {website}.
We are very happy to have you.

Best regards,
{signeture}
"""


def format_msg(
    name: str = "Angela", website: str | None = 'njm.com', sign: str = "Abdullah"
) -> str:
    return msg_format.format(name=name, website=website, signeture=sign)
