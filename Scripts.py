#assign vertex offsets to texture
vertexoffset = []
vertexnormal = []
for i in range(1, C.scene.frame_end+1):
    C.scene.frame_set(i)
    depsgraph = C.evaluated_depsgraph_get()
    eval = C.active_object.evaluated_get(depsgraph)
    evalMesh = eval.to_mesh()
    for v in evalMesh.vertices:
        #worldVertex = C.active_object.matrix_world @ v.co
        #baseWorldVert = basemesh.matrix_world @ basemesh.data.vertices[v.index].co
        vertexoffset.append((v.co.x - basemesh.data.vertices[v.index].co.x))# - basemesh.data.vertices[v.index].co.x))
        vertexoffset.append((v.co.y - basemesh.data.vertices[v.index].co.y)* -1)# - basemesh.data.vertices[v.index].co.z))
        vertexoffset.append((v.co.z - basemesh.data.vertices[v.index].co.z))# - basemesh.data.vertices[v.index].co.y)*-1)
        vertexnormal.append(v.normal.x)
        vertexnormal.append(v.normal.y)
        vertexnormal.append(v.normal.z)
        vertexnormal.append(1.0)
        vertexoffset.append(1.0)
    eval.to_mesh_clear()
    
D.images['Untitled'].pixels = vertexoffset
    

#Make UVs for the offset texture. Math is not right here.
for v in C.active_object.data.vertices:
    for loop in C.active_object.data.loops:
        if loop.vertex_index == v.index:
            print(Vector(((v.index+0.5)/len(C.active_object.data.vertices),0.5)))
            C.active_object.data.uv_layers.active.data[loop.index].uv = Vector(((v.index+0.5)/len(C.active_object.data.vertices),0.5))
