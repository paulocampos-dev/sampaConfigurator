# Serial protocol commands
CMD_NOP = 0x00
CMD_READ = 0x10
CMD_WRITE = 0x20
CMD_ACK = 0x01

# CNC register addresses and sizes
CNC_BASE_ADD = 0x0000 >> 2
CNC_REG_SIZE = 16 + 1

CMD_REG_ADDR = 3  # rw
PULSE_REG_ADDR = 4  # rw
EVT_CFG_REG_ADDR = 7  # rw
SMP_STS1_REG_ADDR = 10  # r
SMP_STS2_REG_ADDR = 11  # r
SMP_CFG_REG_ADDR = 12  # rw
MEM_ERR_REG_ADDR = 14  # r
VER_REG_ADDR = 15  # r
SMP_CFG1_REG_ADDR = 16  # rw

# DM register addresses and sizes
DM_BASE_ADD = 0x0100 >> 2
DM_REG_SIZE = 62 + 1

CNTRL_REG_ADDR = 0  # rw
PKT_REG_ADDRS = [i for i in range(1, 12)]  # PKT0_REG_ADDR to PKT10_REG_ADDR
PKTDAS_REG_ADDR = 12  # r
FIFO_REG_ADDRS = [i for i in range(13, 25)]  # FIFO0_REG_ADDR to FIFO11_REG_ADDR
HPS_REG_ADDR = 25  # rw
STATUS_REG_ADDR = 26  # r
SYNC_REG_ADDRS = [i for i in range(27, 38)]  # SYNC0_REG_ADDR to SYNC10_REG_ADDR
EDGE_SEL_REG_ADDR = 38  # rw
DROP_REG_ADDRS = [i for i in range(39, 51)]  # DROP0_REG_ADDR to DROP11_REG_ADDR
TRUNC_REG_ADDRS = [i for i in range(51, 63)]  # TRUNC0_REG_ADDR to TRUNC11_REG_ADDR

# PLL settings and registers
PLL_BASE_ADD = 0x0200 >> 2
PLL_POLL_REG_ADD = 0x0000  # Operate in polling (1) or waitrequest mode (0)
PLL_STATUS_REG_ADD = 0x0001  # 1 = ready, 0 = busy
PLL_START_REG_ADD = 0x0002  # Start fractional PLL reconfiguration
PLL_CLK_N_REG_ADD = 0x0003  # Denominator (divider)
PLL_CLK_M_REG_ADD = 0x0004  # Numerator (multiplier)
PLL_CLK_W_REG_ADD = 0x0005  # C counter register
PLL_CLK_R_REG_ADD = 0x000A  # C counter 0 readback address

PLL_CLK_IN = 50
PLL_VCO_FREQ = PLL_CLK_IN * (16 + 16) / (5 + 5)  # f_in * (Mhi + Mlo) / (Nhi + Nlo)

# I2C settings and registers
I2C_BASE_ADD = 0x0300 >> 2
PRE_REG_ADDR = 0  # rw
CTR_REG_ADDR = 1  # rw
ADD_REG_ADDR = 2  # rw
TX_REG_ADDR = 3  # rw
RX_REG_ADDR = 4  # r
COM_REG_ADDR = 5  # r
STA_REG_ADDR = 6  # r

I2C_RX_ACK = 0x10
I2C_AL = 0x4

# PLL output numbers
PLL_ADC = 0
PLL_BX = 1
PLL_SO = 2
PLL_RAD_SLVS = 3  # Not connected
PLL_NUM_OUTPUTS = 5

# CNC register arrays and attributes
cnc_reg = [0] * CNC_REG_SIZE
cnc_reg_RO = [
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    False,
]  # Is register read-only?

# DM register arrays and attributes
dm_reg = [0] * DM_REG_SIZE
dm_reg_RO = [
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
]  # Is register read-only?

# Miscellaneous constants
PMADDL = 0x15
PMADDH = 0x16
CHRGADD = 0x17
CHRGWDATL = 0x18
CHRGWDATH = 0x19
CHRGCTL = 0x1A
CHRGRDATL = 0x1B
CHRGRDATH = 0x1C

