'''
Created on Dec 2, 2016

@author: Aaron
'''
import Navigation.prod.Angle as Angle
import math as Math

class ApproximateLocation:
    @staticmethod
    def getDistanceAdjustmentAngle(geographicPositionLatitude, geographicPositionLongitude, assumedLatitude, assumedLongitude, adjustedAltitude):
        localHourAngle = ApproximateLocation._getLocalHourAngle(geographicPositionLongitude, assumedLongitude)
        correctedAltitude = ApproximateLocation._getCorrectedAltitude(geographicPositionLatitude, assumedLatitude, localHourAngle)
        
        distanceAdjustmentAngleValue = adjustedAltitude.getDegrees() - correctedAltitude
        
#         distanceAdjustmentAngle = Angle.Angle()
#         distanceAdjustmentAngle.setDegrees(distanceAdjustmentAngleValue)
        
        distanceAdjustmentAngleValueInMinutes = round(distanceAdjustmentAngleValue * 60, 0)
        return distanceAdjustmentAngleValueInMinutes
     
    @staticmethod
    def getAzimuthAdjustmentAngle():
        return 7
    
    @staticmethod
    def _getLocalHourAngle(geographicPositionLongitude, assumedLongitude):
        return geographicPositionLongitude.getDegrees() - assumedLongitude.getDegrees()
    
    @staticmethod
    def _getCorrectedAltitude(geographicPositionLatitude, assumedLatitude, LHA):
        sinlat = Math.sin(geographicPositionLatitude.getInRadians()) * Math.sin(assumedLatitude.getInRadians())
        coslat = Math.cos(geographicPositionLatitude.getInRadians()) * Math.cos(assumedLatitude.getInRadians()) * Math.cos(Math.radians(LHA))
        
        return Math.degrees(Math.asin(sinlat + coslat))