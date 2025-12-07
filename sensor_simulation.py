import subprocess
import sys

SCRIPTS = [
    "dows-lake.py",
    "fifth-avenue.py",
    "nac.py",
]

def main():
    procs = []
    try:
        # start each sensor script as its own process
        for script in SCRIPTS:
            print(f"Starting {script} ...")
            p = subprocess.Popen([sys.executable, script])
            procs.append(p)

        print("All sensor scripts started.")
        
        for p in procs:
            p.wait()
    except KeyboardInterrupt:
        print("Stopping all sensor scripts...")
        for p in procs:
            p.terminate()
    finally:
        for p in procs:
            try:
                p.wait(timeout=3)
            except Exception:
                pass

if __name__ == "__main__":
    main()
