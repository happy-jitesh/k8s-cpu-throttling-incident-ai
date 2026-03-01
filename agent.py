import time
import subprocess

from observer import get_cpu_usage, is_cpu_throttled
from llm_brain import llm_decide
from actions import increase_cpu_limit, restart_deployment, notify
from config import *

with open("prompts/cpu_prompt.txt") as f:
    SYSTEM_PROMPT = f.read()

last_restart_time = 0


def can_restart():
    global last_restart_time

    if time.time() - last_restart_time < RESTART_COOLDOWN:
        notify("Restart cooldown active ⏳")
        return False

    last_restart_time = time.time()
    return True


def controller_loop():

    notify("CPU Healing Controller Started 🚀")

    while True:

        cpu_output = get_cpu_usage(NAMESPACE, APP_LABEL)

        if not is_cpu_throttled(cpu_output, CPU_THRESHOLD_PERCENT):
            notify("CPU usage normal ✅")
            time.sleep(CHECK_INTERVAL)
            continue

        notify("High CPU usage detected 🔥")
        notify(cpu_output)

        action = llm_decide(cpu_output, SYSTEM_PROMPT)

        notify(f"LLM Decision: {action}")

        if action == "INCREASE_CPU" and can_restart():

            notify("Increasing CPU limit 🚀")

            increase_cpu_limit(
                DEPLOYMENT_NAME,
                NAMESPACE,
                NEW_CPU_LIMIT
            )

            restart_deployment(DEPLOYMENT_NAME, NAMESPACE)

            subprocess.run(
                f"kubectl rollout status deployment {DEPLOYMENT_NAME} -n {NAMESPACE}",
                shell=True
            )

            notify("Healing completed ✅")

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    controller_loop()