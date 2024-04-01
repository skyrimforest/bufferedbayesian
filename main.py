from fastapi import FastAPI
import uvicorn

from bayesian_optimizor import BayesianOptimization
from bayesian_optimizor import UtilityFunction
from experience_buffer import ExpBuffer
from model import config,target
from SkyLogger import get_logger

logger = get_logger("main")

app = FastAPI()

my_buffer = ExpBuffer()
optimizer = BayesianOptimization(
    f=None,
    pbounds={'x': (-2, 6), 'y': (-3, 8)},
    verbose=2,
    random_state=1,
    exp_buffer=my_buffer,
    allow_duplicate_points=True
)
utility = UtilityFunction(kind="ucb", kappa=2.5, xi=0.0)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/getnewconfig")
async def get_newconfig(new_config: config,new_target: target):
    new_config=new_config.model_dump()
    new_target=new_target.model_dump()
    optimizer.register(params=new_config,target=new_target['target'])

    next_point=optimizer.suggest(utility)

    # logger.info(f"now max: {optimizer.max}")
    return next_point


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080)


