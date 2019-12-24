import os
import envkey

env = envkey.fetch_env(os.environ['ENVKEY'], cache_enabled=False)

def export_env():
    print(f'::add-mask::{os.environ["ENVKEY"]}') 
    for k,v in env.items(): 
        print(f'::set-env name={k}::{v}') 
        print(f'::add-mask::{v}') 