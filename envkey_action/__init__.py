import os
import envkey

env = envkey.fetch_env(os.environ['ENVKEY'], cache_enabled=False)
env_file = os.environ['GITHUB_ENV']

def export_env():
    print(f'::add-mask::{os.environ["ENVKEY"]}') 
    with open(env_file, 'a') as f:
        for k,v in env.items(): 
            f.write(f'{k}={v}\n')  
        print(f'::add-mask::{v}') 