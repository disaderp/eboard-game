import smbus
import time

MCP23017_IODIRA = 0x00
MCP23017_IPOLA  = 0x02
MCP23017_GPINTENA = 0x04
MCP23017_DEFVALA = 0x06
MCP23017_INTCONA = 0x08
MCP23017_IOCONA = 0x0A
MCP23017_GPPUA = 0x0C
MCP23017_INTFA = 0x0E
MCP23017_INTCAPA = 0x10
MCP23017_GPIOA = 0x12
MCP23017_OLATA = 0x14

MCP23017_IODIRB = 0x01
MCP23017_IPOLB = 0x03
MCP23017_GPINTENB = 0x05
MCP23017_DEFVALB = 0x07
MCP23017_INTCONB = 0x09
MCP23017_IOCONB = 0x0B
MCP23017_GPPUB = 0x0D
MCP23017_INTFB = 0x0F
MCP23017_INTCAPB = 0x11
MCP23017_GPIOB = 0x13
MCP23017_OLATB = 0x15

class Track:
	def __init__(self, player): #player: 0 - 3
		self.bus = smbus.SMBus(1)

		#   Addr(BIN)      Addr(hex)
		#XXX X  A2 A1 A0
		#010 0  1  1  1      0x27 
		#010 0  1  1  0      0x26 
		#010 0  1  0  1      0x25 
		#010 0  1  0  0      0x24 
		#010 0  0  1  1      0x23 
		#010 0  0  1  0      0x22
		#010 0  0  0  1      0x21
		#010 0  0  0  0      0x20

		self.MCP23017_ADDRESS = 0x20 + player 

		#Configue the register to default value
		for addr in range(22):
			if (addr == 0) or (addr == 1):
				self.bus.write_byte_data(self.MCP23017_ADDRESS, addr, 0xFF)
			else:
				self.bus.write_byte_data(self.MCP23017_ADDRESS, addr, 0x00)
		
		#configue all PinA output
		self.bus.write_byte_data(self.MCP23017_ADDRESS,MCP23017_IODIRA,0x00)

		#configue all PinB output
		self.bus.write_byte_data(self.MCP23017_ADDRESS,MCP23017_IODIRB,0x00)

	def activateField(self, num):
		if num == 0:
			self.bus.write_byte_data(self.MCP23017_ADDRESS,MCP23017_GPIOA,0x00)
			self.bus.write_byte_data(self.MCP23017_ADDRESS,MCP23017_GPIOB,0x00)
		elif num < 8: #0 - 7
			self.bus.write_byte_data(self.MCP23017_ADDRESS,MCP23017_GPIOA,0x01 << (num - 1))
			self.bus.write_byte_data(self.MCP23017_ADDRESS,MCP23017_GPIOB,0x00)
		else:
			self.bus.write_byte_data(self.MCP23017_ADDRESS,MCP23017_GPIOA,0x00)
			self.bus.write_byte_data(self.MCP23017_ADDRESS,MCP23017_GPIOB,0x01 << (num - 8))