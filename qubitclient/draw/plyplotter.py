
from abc import ABC, abstractmethod
import json
import os

class QuantumDataPlyPlotter(ABC):


    def __init__(self, task_type: str):
        self.task_type = task_type
    @abstractmethod
    def plot_result_npy(self, **kwargs):
        pass
    def plot_result_npz(self, **kwargs):
        pass

    def save_plot(self, fig,  task_type: str,save_name: str, save_format: str = "html") -> str:
        if not os.path.exists("./tmp/client/"):
            os.mkdir("./tmp/client/")
        save_path = "./tmp/client/"+"result_"+task_type+"_"+save_name+"."+save_format
        fig.write_html(save_path)
