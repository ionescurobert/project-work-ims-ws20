import autohttpstat
import json
import sys

# Define the number of curl requests
RUNS = 1000


def main():
    global RUNS
    server = "https://192.168.0.158/demopage.html"
    # Pass arguments separated by space
    args = sys.argv[0:]
    total_times = []
    tls_times = []
    avgs = 0
    while RUNS > 0:
        resp = autohttpstat.main(server, args)
        #print(resp)
        total_times.append(resp['time_total'])
        if server.startswith("https"):
            tls_times.append(resp['range_ssl'])
        RUNS -= 1
    #print(total_times)
    print("--------REPORT--------")
    print("Number of runs: " + str(len(total_times)))
    # TLS active
    if server.startswith("https"):
        avg_ssl_time = sum(tls_times)/len(tls_times)
        print("Average TLS time: " + str(avg_ssl_time) + "ms")

    avg_total_time = sum(total_times)/len(total_times)
    print("Average total time: " + str(avg_total_time) + "ms")


if __name__ == '__main__':
    print("Starting TLS Stats")
    main()
