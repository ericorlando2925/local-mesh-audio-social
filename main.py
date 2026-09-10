import asyncio
from bleak import BleakScanner
import random
import time

class LocalMeshAudioNode:
    """
    Mesh node integrating Bluetooth device scanning with 
    real-time voice/audio streaming patterns from awesome-llm-apps.
    """
    def __init__(self, node_id="Node-Voice-01"):
        self.node_id = node_id
        self.is_streaming = False

    def read_environmental_sensors(self):
        # Simulated metrics for your local mesh environment
        light_lux = round(random.uniform(10.0, 300.0), 2)
        presence_detected = random.choice([True, False])
        return light_lux, presence_detected

    async def scan_mesh_peers(self):
        """Scans for nearby peers using Bleak."""
        try:
            devices = await BleakScanner.discover(timeout=2.0)
            return devices
        except Exception as e:
            print(f"[{self.node_id}] BLE Scan note: {e}")
            return []

    async def mock_audio_stream_handler(self):
        """Simulates audio chunk routing across the local mesh network."""
        if self.is_streaming:
            print(f"[{self.node_id}] 🔊 Transmitting audio packet chunk over local mesh...")
        else:
            print(f"[{self.node_id}] 🎙️ Audio channel idle. Listening for peer triggers...")

    async def run(self):
        print(f"=== Starting [{self.node_id}] Local Mesh Audio Node ===")
        
        while True:
            lux, presence = self.read_environmental_sensors()
            peers = await self.scan_mesh_peers()
            
            # Toggle streaming state based on human presence simulation
            self.is_streaming = presence 
            
            print(f"\n--- Node Status [{time.strftime('%X')}] ---")
            print(f" Environment Light : {lux} lux")
            print(f" Human Presence    : {'Active' if presence else 'Away'}")
            print(f" Discovered Peers  : {len(peers)}")
            
            for peer in peers:
                print(f"   -> Peer Node Found: {peer.name or 'Unknown'} [{peer.address}]")
            
            # Execute audio streaming check
            await self.mock_audio_stream_handler()
            
            await asyncio.sleep(5)

if __name__ == "__main__":
    node = LocalMeshAudioNode()
    try:
        asyncio.run(node.run())
    except KeyboardInterrupt:
        print("\nNode stopped.")
