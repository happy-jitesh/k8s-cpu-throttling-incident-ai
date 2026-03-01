import subprocess


def increase_cpu_limit(deployment, namespace, new_limit):

    subprocess.run(
        f"kubectl patch deployment {deployment} -n {namespace} "
        f"--type='json' "
        f"-p='[{{\"op\": \"replace\", "
        f"\"path\": \"/spec/template/spec/containers/0/resources/limits/cpu\", "
        f"\"value\": \"{new_limit}\"}}]'",
        shell=True
    )


def restart_deployment(deployment, namespace):

    subprocess.run(
        f"kubectl rollout restart deployment {deployment} -n {namespace}",
        shell=True
    )


def notify(msg):
    print(f"[NOTIFICATION]: {msg}")