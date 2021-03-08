#assign vertex offsets to texture
vertexoffset = []
vertexnormal = []
for i in range(1, C.scene.frame_end):
    C.scene.frame_set(i)
    depsgraph = C.evaluated_depsgraph_get()
    eval = C.active_object.evaluated_get(depsgraph)
    evalMesh = eval.to_mesh()
    for v in evalMesh.vertices:
        vertexoffset.append((v.co.x - basemesh.data.vertices[v.index].co.x)*100)
        vertexoffset.append((v.co.y - basemesh.data.vertices[v.index].co.y)*-100)
        vertexoffset.append((v.co.z - basemesh.data.vertices[v.index].co.z)*100)
        vertexnormal.append(v.normal.x)
        vertexnormal.append(v.normal.y)
        vertexnormal.append(v.normal.z)
        vertexnormal.append(1.0)
        vertexoffset.append(1.0)
    eval.to_mesh_clear()
    
D.images['Untitled'].pixels = vertexoffset
	

#Make UVs for the offset texture.
for v in C.active_object.data.vertices:
	for loop in C.active_object.data.loops:
		if loop.vertex_index == v.index:
			print(Vector(((v.index+0.5)/len(C.active_object.data.vertices),0.5)))
			C.active_object.data.uv_layers.active.data[loop.index].uv = Vector(((v.index+0.5)/len(C.active_object.data.vertices),0.5))
