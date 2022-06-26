import datetime
import time
from skyfield.api import load, Topos, EarthSatellite

TLE_FILE = "https://celestrak.com/NORAD/elements/active.txt"
ISS_NAME = "ISS (ZARYA)"
LONGITUDE = -90.230759
LATITUDE = 15.783471

class SatelliteObserver:

    def __init__(self, where: Topos, what: EarthSatellite):
        self.where = where
        self.sat = what
        self.sat_name = what.name
        self.ts = load.timescale(builtin=True)

    @classmethod
    def from_strings(cls, longitude: str or float, latitude: str or float, sat_name: str, tle_file: str) -> 'SatelliteObserver':
        place = Topos(latitude, longitude)
        satellites = load.tle(tle_file)
        print("loaded {} sats from {}".format(len(satellites), tle_file))
        _sats_by_name = {sat.name: sat for sat in satellites.values()}
        satellite = _sats_by_name[sat_name]
        return cls(place, satellite)

    def altAzDist_at(self, at: float) -> (float, float, float):
        """
        :param at: Unix time GMT (timestamp)
        :return: (altitude, azimuth, distance)
        """
        current_gmt = datetime.datetime.utcfromtimestamp(at)
        current_ts = self.ts.utc(current_gmt.year, current_gmt.month, current_gmt.day, current_gmt.hour,
                            current_gmt.minute, current_gmt.second + current_gmt.microsecond / 1000000.0)
        difference = self.sat - self.where
        observer_to_sat = difference.at(current_ts)
        altitude, azimuth, distance = observer_to_sat.altaz()
        return (altitude.degrees, azimuth.degrees, distance.km)

    def current_altAzDist(self) -> (float, float, float):
        return self.altAzDist_at(time.mktime(time.gmtime()))

    def above_horizon(self, at: float) -> bool:
        """
        :param at: Unix time GMT
        :return:
        """
        (alt, az, dist) = self.altAzDist_at(at)
        return alt > 0


def main():
    iss = SatelliteObserver.from_strings(LONGITUDE, LATITUDE, ISS_NAME, TLE_FILE)
    elevation, azimuth, distance = iss.current_altAzDist()
    visible = "visible!" if elevation > 0 else "not visible =/"
    print("ISS from latitude {}, longitude {}: azimuth {}, elevation {} ({})".format(LATITUDE, LONGITUDE, azimuth, elevation, visible))

if __name__ == "__main__":
    main()
