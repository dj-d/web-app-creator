import os
import argparse
import subprocess

from lib.dataclasses import (
    RunConfig,
    DesktopConfig,
    LinkConfig
)

from lib.constants import (
    OPT_PATH
)

def create_run(working_dir: str, config: RunConfig) -> str:
    model = f"""#!/bin/bash
                nohup google-chrome-stable --new-window --app={config.url} >/dev/null 2>&1 &
                """
    
    path = f'{working_dir}/{config.startup_class}.sh'
    with open(path, 'w') as f:
        f.write(model)

    return path

def create_destop(working_dir: str, config: DesktopConfig) -> str:
    os.system(f'cp {config.icon_path} {working_dir}/.')

    icon_path = f'{working_dir}/{config.icon_path.split("/")[-1]}'

    model = f"""[Desktop Entry]
                Name={config.name}
                StartupWMClass={config.startup_class}
                Exec={config.exec_path if config.exec_path else f'/usr/bin/{config.startup_class}'}
                Icon={icon_path}
                Path={config.path}
                Comment={config.comment}
                Type={config.type}
                Categories={config.categories}
                """
    
    path = f'{working_dir}/{config.startup_class}.desktop'
    with open(path, 'w') as f:
        f.write(model)
    
    return path

def create_links(config: LinkConfig) -> None:
    subprocess.run(f'sudo ln -s {config.run_path} /usr/bin/{config.startup_class}', shell=True)
    subprocess.run(f'sudo ln -s {config.desktop_path} /usr/share/applications/.', shell=True)

def main(run_config: RunConfig, desktop_config: DesktopConfig, custom_path: str = None) -> None:
    if custom_path:
        working_dir = f'{custom_path}'
    else:
        working_dir = f'{OPT_PATH}/{desktop_config.startup_class}'

    os.system(f'mkdir -p {working_dir}')

    run_path = create_run(
        working_dir=working_dir, 
        config=run_config
        )
    
    os.system(f'chmod +x {run_path}')
    
    desktop_path = create_destop(
        working_dir=working_dir, 
        config=desktop_config
        )

    create_links(config=LinkConfig(run_path, desktop_path, desktop_config.startup_class))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        '--url',
        dest='url',
        required=True,
        type=str,
        help='WebApp URL'
    )

    parser.add_argument(
        '--name',
        dest='name',
        required=True,
        type=str,
        help='Name of WebApp'
    )

    parser.add_argument(
        '--startup-class',
        dest='startup_class',
        required=True,
        type=str,
        help='Startup Class of WebApp (ex: Slack -> slack or Google Calendar -> google-calendar)'
    )

    parser.add_argument(
        '--icon-path',
        dest='icon_path',
        required=True,
        type=str,
        help='Icon Path of WebApp'
    )

    parser.add_argument(
        '--exec-path',
        dest='exec_path',
        required=False,
        type=str,
        help='Exec Path of WebApp'
    )

    parser.add_argument(
        '--path',
        dest='path',
        required=False,
        type=str,
        help='Path of WebApp'
    )

    parser.add_argument(
        '--comment',
        dest='comment',
        required=False,
        type=str,
        help='Comment of WebApp'
    )

    parser.add_argument(
        '--type',
        dest='type',
        required=False,
        type=str,
        help='Type of WebApp'
    )

    parser.add_argument(
        '--categories',
        dest='categories',
        required=False,
        type=str,
        help='Categories of WebApp'
    )

    parser.add_argument(
        '--custom-path',
        dest='custom_path',
        required=False,
        type=str,
        help='Custom Path of WebApp'
    )

    args = parser.parse_args()

    run_config = RunConfig(
        url=args.url,
        startup_class=args.startup_class
    )

    desktop_config = DesktopConfig(
        working_dir=args.custom_path if args.custom_path else OPT_PATH,
        name=args.name,
        startup_class=args.startup_class,
        icon_path=args.icon_path,
        exec_path=args.exec_path,
        path=args.path,
        comment=args.comment,
        type=args.type,
        categories=args.categories
    )

    main(
        run_config=run_config,
        desktop_config=desktop_config,
        custom_path=args.custom_path
    )
