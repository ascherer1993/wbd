'''
Created on Dec 2, 2016

@author: Aaron
'''
import Navigation.prod.Angle as Angle
import math as Math

class ApproximateLocation:
    @staticmethod
    def getDistanceAdjustmentAngle(geographicPositionLatitude, geographicPositionLongitude, assumedLatitude, assumedLongitude, adjustedAltitude, returnAngle = False):
        localHourAngle = ApproximateLocation._getLocalHourAngle(geographicPositionLongitude, assumedLongitude)
        
        sinlat = Math.sin(geographicPositionLatitude.getInRadians()) * Math.sin(assumedLatitude.getInRadians())
        coslat = Math.cos(geographicPositionLatitude.getInRadians()) * Math.cos(assumedLatitude.getInRadians()) * Math.cos(Math.radians(localHourAngle))
        
        intermediateDistance = sinlat + coslat
        
        correctedAltitude = Math.degrees(Math.asin(intermediateDistance))
        
        distanceAdjustmentAngleValue = adjustedAltitude.getDegrees() - correctedAltitude
        
#         distanceAdjustmentAngle = Angle.Angle()
#         distanceAdjustmentAngle.setDegrees(distanceAdjustmentAngleValue)
        
        distanceAdjustmentAngleValueInMinutes = round(distanceAdjustmentAngleValue * 60, 0)
        return distanceAdjustmentAngleValueInMinutes
     
    @staticmethod
    def getAzimuthAdjustmentAngle(geographicPositionLatitude, assumedLatitude, distanceAdjustmentAngle):
        azimuthAdjustmentAngle = Angle.Angle()
        return azimuthAdjustmentAngle
    
    @staticmethod
    def _getLocalHourAngle(geographicPositionLongitude, assumedLongitude):
        return geographicPositionLongitude.getDegrees() - assumedLongitude.getDegrees()
    
