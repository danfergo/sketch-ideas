import pymunk


class Robot:

    def __init__(self, position):
        self.position = position

    def build(self):
        position = self.position

        rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        rotation_center_body.position = position

        body = pymunk.Body()
        body.position = position
        l1 = pymunk.Segment(body, (0.0, 0), (50.0, 0.0), 1.0)
        l1.density = 1

        joint11 = pymunk.PinJoint(rotation_center_body, body, (0, 0), (0, 0))
        joint12 = pymunk.SimpleMotor(rotation_center_body, body, 0)
        joint12.rate = 1.0

        body2 = pymunk.Body()
        body2.position = (position[0] + 50, position[1])
        l2 = pymunk.Segment(body2, (0.0, 0), (50.0, 0.0), 1.0)
        l2.density = 1

        joint21 = pymunk.PinJoint(body, body2, (50.0, 0), (0, 0))
        joint22 = pymunk.SimpleMotor(body, body2, 0)

        joint22.rate = 1.0

        return l1, joint11, joint12, body, \
               l2, joint21, joint22, body2
