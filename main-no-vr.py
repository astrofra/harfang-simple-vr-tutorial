# Open a scene

import harfang as hg

hg.InputInit()
hg.WindowSystemInit()

res_x, res_y = 1280, 720
win = hg.RenderInit('PBR Scene', res_x, res_y, hg.RF_VSync | hg.RF_MSAA4X)

#
pipeline = hg.CreateForwardPipeline()
res = hg.PipelineResources()

hg.AddAssetsFolder("resources_compiled")

# load scene
scene = hg.Scene()
hg.LoadSceneFromAssets("pharao/scene_Sketchfab_Scene.scn", scene, res, hg.GetForwardPipelineInfo())

# add a camera
cam = hg.CreateCamera(scene, hg.TransformationMat4(hg.Vec3(0, 1.0, -5), hg.Vec3(hg.Deg(12), 0, 0)), 0.01, 1000)
scene.SetCurrentCamera(cam)

# main loop
while not hg.ReadKeyboard().Key(hg.K_Escape):
	dt = hg.TickClock()

	scene.Update(dt)
	hg.SubmitSceneToPipeline(0, scene, hg.IntRect(0, 0, res_x, res_y), True, pipeline, res)

	hg.Frame()
	hg.UpdateWindow(win)

hg.RenderShutdown()
hg.DestroyWindow(win)
