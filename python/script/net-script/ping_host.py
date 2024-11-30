from collections.abc import Iterator
import subprocess
import argparse
import ipaddress
from concurrent.futures import ThreadPoolExecutor


def ping_host(ip: str) -> str | None:
    """
    Pings a single host and returns the IP if it is reachable.
    """
    try:
        output = subprocess.run(
            ["ping", "-c", "1", "-w", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if output.returncode == 0:
            return ip
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
    return None


def ping_subnet(subnet: str, worker: int) -> list[str]:
    """
    Pings all hosts within the given subnet and returns a list of reachable IPs.
    """
    reachable_hosts = []
    print("Pinging all hosts in the subnet. Please wait...")

    with ThreadPoolExecutor(max_workers=worker) as executor:
        results = executor.map(ping_host, generate_ips(subnet))

    reachable_hosts = [ip for ip in results if ip is not None]
    return reachable_hosts


def generate_ips(cidr: str) -> Iterator[str]:
    network = ipaddress.IPv4Network(cidr, strict=False)
    for ip in network.hosts():
        yield str(ip)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ip-listener", description="simple multi-thread ping within subnet"
    )
    parser.add_argument("-c", "--cidr")
    parser.add_argument("-w", "--worker", type=int, default=20)
    args = parser.parse_args()

    print("cidr:", args.cidr)
    print("worker:", args.worker)
    reachable_hosts = ping_subnet(args.cidr, args.worker)
    print("Reachable hosts:")
    for host in reachable_hosts:
        print(host)
