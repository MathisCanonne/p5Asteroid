def setup():
    print("START-------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    core.memory("position", vector2(400, 400))
    core.memory("vitesse", vector2(1, 0))
    print("Setup END-----")

def run():
    core.cleanScreen()

    core.memory('position',core.memory('position')+core.memory("vitesse"))

    core.draw.polygon((255, 0, 0), (P1, P2, P3))

    if core.getKeyPressList("z"):
        core.memory("vitesse").scale_to_length(core.memory("vitesse").length()+0.1 )

    if core.getKeyPressList("d"):
        core.memory("vitesse", core.memory("vitesse").rotate(5))

    vectP1 = core.memory("vitesse").rotate(90)
    vectP1.scale_to_length(10)
    P1=core.memory("position") + vectP1

    vectP2 = vector2(core.memory("vitesse"))
    vectP2.scale_to_length(15)
    P2 = core.memory("position") + vectP2

    vectP3 = core.memory("vitesse").rotate(-90)
    vectP3.scale_to_length(10)
    P3 = core.memory("position") + vectP3

    

