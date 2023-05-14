#!/usr/bin/env python
from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

store = ModbusSlaveContext(
	di = ModbusSequentialDataBlock(0,[17]*100), 
#initializer
	co = ModbusSequentialDataBlock(0,[17]*100),
	hr = ModbusSequentialDataBlock(0,[17]*100),
#initalizer
	ir = ModbusSequentialDataBlock(0,[17]*100))
#initalizer
context = ModbusServerContext(slaves=store, single=True)

identity = ModbusDeviceIdentification()
identity.VendorName = 'PyModbus Inc.'
identity.ProductCode = 'PM'
identity.VendorUrl = 'https://github.com/riptideio/pyModbus'
identity.ProductName = 'Modbus Server'
identity.ModelName = 'PyModbus'
identity.MajorMinorRevision = '1.0'

print ("starting Modbus server...")
StartTcpServer(context,identity=identity,address=("0.0.0.0",502))