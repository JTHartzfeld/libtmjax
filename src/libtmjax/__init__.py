'''libtmjax: Library for TileMaps (JSON And XML)

The library provides facilites load, manipulate, and save files in .tmx and .tm.json (.tmj)
files.

'''



class TileMap:
    ''''''

    def __init__(self, *args, **kwargs):
        self.version            = kwargs.get("version",             "1.0")
        self.tiledversion       = kwargs.get("tiledversion",        "1.0.1")
        self.class_             = kwargs.get("class_",              "")
        self.orientation        = kwargs.get("orientation",         "orthogonal")
        self.renderorder        = kwargs.get("renderoroder",        "right-down")
        self.compressionlevel   = kwargs.get("compressionlevel",     -1)
        self.width              = kwargs.get("width",               100)
        self.height             = kwargs.get("height",              100)
        self.tilewidth          = kwargs.get("tilewidth",            32)
        self.tileheight         = kwargs.get("tileheight",           32)
        self.hexsidelength      = kwargs.get("hexsidelength",
                                             kwargs.get("hexsidelen", 32))
        self.staggeraxis        = kwargs.get("staggeraxis",         "x")
        self.staggerindex       = kwargs.get("staggerindex",        "even")
        self.parallaxoriginx    = kwargs.get("parallaxoriginx",     0)
        self.parallaxoriginy    = kwargs.get("parallaxoriginy",     0)
        self.backgroundcolor    = kwargs.get("backgroundcolor",
                                             kwargs.get("bgcolor", "#00000000"))
        self.nextlayerid        = kwargs.get("nextlayerid",         1)
        self.nextobjectid       = kwargs.get("nextobjectid",        1)
        self.infinite           = kwargs.get("infinite",            0)

class TileSet:
    def __init__(self, **kwargs):
        self.firstgid           = kwargs.get("fistgid",             1)
        self.source             = kwargs.get("source",              "")
        self.name               = kwargs.get("name",                "")
        self.class_             = kwargs.get("class_",              "")
        self.tilewidth          = kwargs.get("tilewidth",           32)
        self.tileheight         = kwargs.get("tileheight",          32)
        self.spacing            = kwargs.get("spacing",             0)
        self.margin             = kwargs.get("margin",              0)
        self.tilecount          = kwargs.get("tilecount",           1)
        self.columns            = kwargs.get("columns",             1)
        self.objectalignment    = kwargs.get("objectalignment",     "unspecified")
        self.tilerendersize     = kwargs.get("tilerendersize",      "tile")
        self.fillmode           = kwargs.get("fillmode",            "stretch")
        
        
        

class Tile:
    pass

class MapObject:
    pass

class MapLayer:
    pass

class TileLayer(MapLayer):
    pass

class ObjectLayer(MapLayer):
    pass

