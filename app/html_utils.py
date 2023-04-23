def build_html_chat(is_me, character, text):
    me_avatar = "static/avatar_user.png"
    if character == 'yoda':
        bot_avatar = "static/avatar_yoda.png"
    if character == 'sponge_bob':
        bot_avatar = "static/avatar_sponge_bob.png"

    if is_me:
        html_message = (
            '<li style="width:100%">' +
            '<div class="msj macro">' +
            '<div class="avatar">'
            '<img class="img-circle" style="width:100%;" src="' + me_avatar + '" />' +
            '</div>' +
            '<div class="text text-l">' +
            '<p>' + text + '</p>' +
            '</div>' +
            '</div>' +
            '</li>'
        )

    else:
        html_message = (
            '<li style="width:100%;">' +
            '<div class="msj-rta macro">' +
            '<div class="text text-r">' +
            '<p>' + text + '</p>' +
            '</div>' +
            '<div class="avatar" style="padding:0px 0px 0px 10px !important">' +
            '<img class="img-circle" style="width:100%;" src="' + bot_avatar + '" />' +
            '</div>' +
            '</div>' +
            '</li>'
        )

    return html_message
