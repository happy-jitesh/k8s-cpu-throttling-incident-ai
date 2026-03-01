import subprocess


def get_cpu_usage(namespace, label):

    cmd = f"kubectl top pods -n {namespace} -l {label}"
    output = subprocess.getoutput(cmd)

    return output


def is_cpu_throttled(cpu_output, threshold_percent):

    lines = cpu_output.split("\n")

    if len(lines) <= 1:
        return False

    for line in lines[1:]:  # skip header
        parts = line.split()

        if len(parts) < 2:
            continue

        cpu_value = parts[1]

        if cpu_value.endswith("m"):
            cpu_millicores = int(cpu_value.replace("m", ""))

            # assuming 100m original limit
            if cpu_millicores >= threshold_percent:
                return True

    return False