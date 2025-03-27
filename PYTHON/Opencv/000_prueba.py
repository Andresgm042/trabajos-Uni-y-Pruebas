import cv2
import torch
import subprocess

def check_opencv_cuda():
    print("🔹 Verificando OpenCV con CUDA...")
    try:
        if cv2.cuda.getCudaEnabledDeviceCount() > 0:
            print("✅ OpenCV detecta CUDA")
        else:
            print("❌ OpenCV NO detecta CUDA")
    except Exception as e:
        print(f"❌ Error con OpenCV: {e}")

def check_pytorch_cuda():
    print("\n🔹 Verificando PyTorch con CUDA...")
    if torch.cuda.is_available():
        print(f"✅ PyTorch detecta CUDA - {torch.cuda.get_device_name(0)}")
    else:
        print("❌ PyTorch NO detecta CUDA")

def check_cuda():
    print("\n🔹 Verificando CUDA con 'nvcc'...")
    try:
        result = subprocess.run(["nvcc", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "release" in result.stdout:
            print(f"✅ CUDA está instalado:\n{result.stdout}")
        else:
            print("❌ CUDA NO está disponible")
    except FileNotFoundError:
        print("❌ CUDA NO está instalado (comando 'nvcc' no encontrado)")

if __name__ == "__main__":
    check_opencv_cuda()
    check_pytorch_cuda()
    check_cuda()
