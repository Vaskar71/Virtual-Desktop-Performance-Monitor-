import tkinter as tk         # For GUI components.
from tkinter import ttk      # For themed tkinter widgets.
import psutil                # To fetch system performance metrics.
import datetime              # To add timestamps to our data.
import csv                   # For logging data to CSV files.
import os                    # To handle file system operations.

class PerformanceMonitor:
    def __init__(self):
        # Initialization can be extended if needed.
        pass

    def get_cpu_usage(self):
        """
        Returns the CPU usage percentage.
        psutil.cpu_percent waits for 1 second to measure usage accurately.
        """
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        """
        Returns the memory usage percentage.
        """
        memory = psutil.virtual_memory()
        return memory.percent

    def get_network_usage(self):
        """
        Returns the total bytes sent and received since boot.
        """
        net_io = psutil.net_io_counters()
        return net_io.bytes_sent, net_io.bytes_recv

    def get_all_metrics(self):
        """
        Retrieves all metrics and returns them as a dictionary.
        """
        cpu = self.get_cpu_usage()
        memory = self.get_memory_usage()
        sent, recv = self.get_network_usage()
        return {
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'cpu': cpu,
            'memory': memory,
            'bytes_sent': sent,
            'bytes_recv': recv
        }
class CSVLogger:
    def __init__(self, filename="performance_log.csv"):
        self.filename = filename
        # Create the CSV file with headers if it does not exist.
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "CPU Usage (%)", "Memory Usage (%)", "Bytes Sent", "Bytes Received"])

    def log(self, data):
        """
        Appends a new row of data to the CSV file.
        'data' should be a dictionary with keys: timestamp, cpu, memory, bytes_sent, bytes_recv.
        """
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                data['timestamp'], 
                data['cpu'], 
                data['memory'], 
                data['bytes_sent'], 
                data['bytes_recv']
            ])
class PerformanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Desktop Performance Monitor")

        # Initialize performance monitoring and logging.
        self.monitor = PerformanceMonitor()
        self.logger = CSVLogger()

        # Set up the GUI components.
        self.create_widgets()

        # Start the periodic update of metrics.
        self.update_metrics()

    def create_widgets(self):
        """
        Creates and places all the widgets in the window.
        """
        # Label for CPU usage.
        self.cpu_label = ttk.Label(self.root, text="CPU Usage: ")
        self.cpu_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        # Label for Memory usage.
        self.memory_label = ttk.Label(self.root, text="Memory Usage: ")
        self.memory_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        # Label for Network usage (bytes sent and received).
        self.network_label = ttk.Label(self.root, text="Network Usage (Sent / Recv): ")
        self.network_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        # Text widget to display log entries.
        self.log_text = tk.Text(self.root, height=10, width=50)
        self.log_text.grid(row=3, column=0, padx=10, pady=10)

    def update_metrics(self):
        """
        Fetches the latest metrics, updates the GUI, logs the data, and schedules the next update.
        """
        try:
            # Get current performance metrics.
            data = self.monitor.get_all_metrics()

            # Update GUI labels with the new metrics.
            self.cpu_label.config(text=f"CPU Usage: {data['cpu']}%")
            self.memory_label.config(text=f"Memory Usage: {data['memory']}%")
            self.network_label.config(
                text=f"Network Usage (Sent: {data['bytes_sent']} bytes / Recv: {data['bytes_recv']} bytes)"
            )

            # Log the metrics to CSV.
            self.logger.log(data)

            # Add a log entry to the text widget.
            log_entry = (f"{data['timestamp']} | CPU: {data['cpu']}% | Memory: {data['memory']}% | "
                         f"Sent: {data['bytes_sent']} | Recv: {data['bytes_recv']}\n")
            self.log_text.insert(tk.END, log_entry)
            self.log_text.see(tk.END)  # Auto-scroll to the latest entry.

        except Exception as e:
            # Display any errors in the text widget.
            error_message = f"Error retrieving metrics: {e}\n"
            self.log_text.insert(tk.END, error_message)
            self.log_text.see(tk.END)

        # Schedule the next update in 1 second (1000 milliseconds).
        self.root.after(1000, self.update_metrics)
if __name__ == "__main__":
    # Create the main Tkinter window.
    root = tk.Tk()

    # Instantiate the PerformanceApp with the root window.
    app = PerformanceApp(root)

    # Start the Tkinter event loop.
    root.mainloop()
