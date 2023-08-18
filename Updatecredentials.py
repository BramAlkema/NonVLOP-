from mastodon import Mastodon

#Mastodon.create_app(
#     'pytooterapp',
#     api_base_url = 'https://mastodon.xn--sft219bi3tzwd.com',
#     to_file = 'pytooter_clientcred.secret'
#)

mastodon = Mastodon(
    client_id = 'pytooter_clientcred.secret',
    api_base_url = 'https://mastodon.xn--sft219bi3tzwd.com'
)


mastodon.log_in(
    'lolazeizolda@example.net',
    'henkhenk',
    to_file = 'pytooter_usercred.secret'
)


mastodon = Mastodon(
    access_token = 'pytooter_usercred.secret',
    api_base_url = 'https://mastodon.xn--sft219bi3tzwd.com'
)
mastodon.toot('Updaterts')
mastodon.account_update_credentials(display_name='Lola',
    note="Nonefdfdf dfdf ",
    avatar=None,
    avatar_mime_type=None,
    header=None,
    header_mime_type=None,
    locked=None,
    bot=None,
    discoverable=None,
    fields=None)
