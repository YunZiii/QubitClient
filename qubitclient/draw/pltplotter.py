import os
from abc import ABC, abstractmethod

class QuantumDataPltPlotter(ABC):
    def __init__(self, task_type: str):
        self.task_type = task_type


    @abstractmethod
    def plot_result_npy(self, **kwargs):
        pass

    def plot_result_npz(self, **kwargs):
        pass

    def save_plot(self, fig, task_type: str,save_name: str,save_format: str = "png"):
        if not os.path.exists("./tmp/client/"):
            os.mkdir("./tmp/client/")
        save_path = "./tmp/client/" + "result_" + task_type + "_" + save_name + "." + save_format
        fig.savefig(save_path)
