layer = iface.activeLayer()

allfeatures={}
index = QgsSpatialIndex()
for ft in layer.getFeatures():
    allfeatures[ft.id()] = ft
    index.insertFeature(ft)

selection = []
for feat in layer.getFeatures():
    inGeom = feat.geometry()
    idsList = index.intersects(inGeom.boundingBox())
    if len(idsList) > 1:
        for id in idsList:
            selection.append(allfeatures[id])


layer.selectByIds([k.id() for k in selection])