import pymunk


class World:

    def build(self):
        rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        rotation_center_body.position = (300, 300)

        rotation_limit_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        rotation_limit_body.position = (200, 300)

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (10, 10)
        l1 = pymunk.Segment(body, (0, 0), (580, 0), 5.0)

        return l1, body