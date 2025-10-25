from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class EntityWatchlistCode(str, Enum):
    ca_con = "CA_CON"
    eu_con = "EU_CON"
    iz_soe = "IZ_SOE"
    iz_unc = "IZ_UNC"
    us_cap = "US_CAP"
    us_fse = "US_FSE"
    us_mbs = "US_MBS"
    us_sdn = "US_SDN"
    us_ssi = "US_SSI"
    us_cmc = "US_CMC"
    us_uvl = "US_UVL"
    au_con = "AU_CON"
    uk_hmc = "UK_HMC"
