def on_on_chat():
    mobs.clear_effect(mobs.target(LOCAL_PLAYER))
player.on_chat("unvanish", on_on_chat)

def on_on_chat2():
    mobs.apply_effect(INVISIBILITY, mobs.target(LOCAL_PLAYER), 600, 255)
player.on_chat("vanish", on_on_chat2)

player.say("deze server gebruikt de vanish plugin")