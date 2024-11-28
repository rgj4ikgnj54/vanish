player.onChat("unvanish", function () {
    mobs.clearEffect(mobs.target(LOCAL_PLAYER))
})
player.onChat("vanish", function () {
    mobs.applyEffect(INVISIBILITY, mobs.target(LOCAL_PLAYER), 600, 255)
})
player.say("deze server gebruikt de vanish plugin")
