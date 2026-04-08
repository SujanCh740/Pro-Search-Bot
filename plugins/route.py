from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("BenFilterBot")

@routes.get("/verify")
async def verify_handler(request):
    return web.FileResponse('verify.html')
