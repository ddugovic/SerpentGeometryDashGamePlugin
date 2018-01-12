from serpent.game import Game

from .api.api import GeometryDashAPI

from serpent.utilities import Singleton




class SerpentGeometryDashGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "Geometry Dash"

        kwargs["app_id"] = "322170"
        kwargs["app_args"] = None

        super().__init__(**kwargs)

        self.api_class = GeometryDashAPI
        self.api_instance = None

        self.frame_transformation_pipeline_string = "RESIZE:128x96|GRAYSCALE"

        self.frame_width = 128
        self.frame_height = 96
        self.frame_channels = 0

        #query_sprite = Sprite("QUERY", image_data=query_image[])
        #self.viridian = self.sprite_identifier.identify(query_sprite, mode="SIGNATURE_COLORS")

    @property
    def screen_regions(self):
        regions = {
            "HP_AREA": (8, 180, 16, 460),
            "SCORE_AREA": (8, 180, 14, 460)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
