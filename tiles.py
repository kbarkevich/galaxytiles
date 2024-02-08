
class TileList:
    Blank = {
        'NAME': '',
        'IMG': 'images/background.png',
        'REQS': []
    }

    HallwaySegment = {
        'NAME': 'HallwaySegment',
        'IMG': 'images/hallwaysegment.png',
        'REQS': []
    }

    HallwaySegmentChest = {
        'NAME': 'HallwaySegmentChest',
        'IMG': 'images/hallwaysegmentchest.png',
        'REQS': [
            [7, ">CONTAINER_CONTENTS"]
        ]
    }

    HallwaySegmentDoor = {
        'NAME': 'HallwaySegmentDoor',
        'IMG': 'images/hallwaysegmentdoor.png',
        'REQS': [
            [3, ">ATTRS_BOOL", ["DoorSensor"]]
        ]
    }

    HallwaySegmentDoorSign = {
        'NAME': 'HallwaySegmentDoorSign',
        'IMG': 'images/hallwaysegmentdoorsign.png',
        'REQS': [
            [3, ">ATTRS_BOOL", ["DoorSensor"]],
            [4, "Text", ["SignPanel", "SurfaceGui", "Frame", "TextLabel"]],
            [4, "Color", ["SignBody"]]
        ]
    }

    HallwayThreeWayJunction = {
        'NAME': 'HallwayThreeWayJunction',
        'IMG': 'images/hallwaythreewayjunction.png',
        'REQS': []
    }

    HallwayThreeWayJunctionWithSign = {
        'NAME': 'HallwayThreeWayJunctionWithSign',
        'IMG': 'images/hallwaythreewayjunction1sign.png',
        'REQS': [
            [3, "Text", ["SignPanel", "SurfaceGui", "Frame", "TextLabel"]],
            [3, "Color", ["SignBody"]]
        ]
    }

    HallwayThreeWayJunctionWith2Signs = {
        'NAME': 'HallwayThreeWayJunctionWith2Signs',
        'IMG': 'images/hallwaythreewayjunction2signs.png',
        'REQS': [
            [3, "Text", ["SignPanel", "SurfaceGui", "Frame", "TextLabel"]],
            [3, "Color", ["SignBody"]],
            [4, "Text", ["SignPanel", "SurfaceGui", "Frame", "TextLabel"]],
            [4, "Color", ["SignBody"]]
        ]
    }

    HallwayThreeWayJunctionWith3Signs = {
        'NAME': 'HallwayThreeWayJunctionWith3Signs',
        'IMG': 'images/hallwaythreewayjunction3signs.png',
        'REQS': [
            [3, "Text", ["SignPanel", "SurfaceGui", "Frame", "TextLabel"]],
            [3, "Color", ["SignBody"]],
            [4, "Text", ["SignPanel", "SurfaceGui", "Frame", "TextLabel"]],
            [4, "Color", ["SignBody"]],
            [5, "Text", ["SignPanel", "SurfaceGui", "Frame", "TextLabel"]],
            [5, "Color", ["SignBody"]]
        ]
    }

    HallwayFourWayJunction = {
        'NAME': 'HallwayFourWayJunction',
        'IMG': 'images/hallwayfourwayjunction.png',
        'REQS': []
    }

    HallwayCorner = {
        'NAME': 'HallwayCorner',
        'IMG': 'images/hallwaycorner.png',
        'REQS': []
    }

    HallwayCornerWindows = {
        'NAME': 'HallwayCornerWindows',
        'IMG': 'images/hallwaycornerwindows.png',
        'REQS': []
    }

    HallwayDeskOpenable = {
        'NAME': 'HallwayDeskOpenable',
        'IMG': 'images/hallwaydeskopenable.png',
        'REQS': [
            [5, ">ATTRS_BOOL", ["DoorSensor"]]
        ]
    }

    HallwayDeskOpenableSign = {
        'NAME': 'HallwayDeskOpenableSign',
        'IMG': 'images/hallwaydeskopenablesign.png',
        'REQS': [
            [5, ">ATTRS_BOOL", ["DoorSensor"]],
            [6, "Text", ["SignPanel", "SurfaceGui", "Frame", "TextLabel"]],
            [6, "Color", ["SignBody"]],
        ]
    }

    RoomEntranceLeft = {
        'NAME': 'RoomEntranceLeft',
        'IMG': 'images/roomentranceleft.png',
        'REQS': []
    }

    RoomEntranceMiddle = {
        'NAME': 'RoomEntranceMiddle',
        'IMG': 'images/roomentrancemiddle.png',
        'REQS': []
    }

    RoomWall = {
        'NAME': 'RoomWall',
        'IMG': 'images/roomwall.png',
        'REQS': []
    }

    RoomWallBench = {
        'NAME': 'RoomWallBench',
        'IMG': 'images/roomwallbench.png',
        'REQS': []
    }

    RoomCorner = {
        'NAME': 'RoomCorner',
        'IMG': 'images/roomcorner.png',
        'REQS': []
    }

    RoomCornerWindows = {
        'NAME': 'RoomCornerWindows',
        'IMG': 'images/roomcornerwindows.png',
        'REQS': []
    }

    RoomCenter = {
        'NAME': 'RoomCenter',
        'IMG': 'images/roomcenter.png',
        'REQS': []
    }

    HallwaySegmentSpawn = {
        'NAME': 'HallwaySegmentSpawn',
        'IMG': 'images/hallwaysegmentspawn.png',
        'REQS': []
    }

    RoomWallSpawn = {
        'NAME': 'HallwaySegmentThreeWayJunctionSpawn',
        'IMG': 'images/roomwallspawn.png',
        'REQS': []
    }

    RoomCenterSpawn = {
        'NAME': 'HallwaySegmentFourWayJunctionSpawn',
        'IMG': 'images/roomcenterspawn.png',
        'REQS': []
    }

    RoomCornerSpawn = {
        'NAME': 'RoomCornerSpawn',
        'IMG': 'images/roomcornerspawn.png',
        'REQS': []
    }

    RoomCornerWindowsSpawn = {
        'NAME': 'RoomCornerWindowsSpawn',
        'IMG': 'images/roomcornerwindowsspawn.png',
        'REQS': []
    }

    RoomEntranceMiddleSpawn = {
        'NAME': 'RoomEntranceMiddleSpawn',
        'IMG': 'images/roomentrancemiddlespawn.png',
        'REQS': []
    }

    HallwaySegmentExhaustVent = {
        'NAME': 'HallwaySegmentExhaustVent',
        'IMG': 'images/hallwaysegmentexhaustvent.png',
        'REQS': []
    }

    HallwaySegmentAirFilter = {
        'NAME': 'HallwaySegmentAirFilter',
        'IMG': 'images/hallwaysegmentairfilter.png',
        'REQS': []
    }

    HallwaySegmentLadderEnd = {
        'NAME': 'HallwaySegmentLadderEnd',
        'IMG': 'images/hallwaysegmentladderend.png',
        'REQS': []
    }

    HallwaySegmentLadder = {
        'NAME': 'HallwaySegmentLadder',
        'IMG': 'images/hallwaysegmentladder.png',
        'REQS': []
    }

    HallwaySegmentLadderStart = {
        'NAME': 'HallwaySegmentLadderStart',
        'IMG': 'images/hallwaysegmentladderstart.png',
        'REQS': []
    }

    HallwaySegmentCap = {
        'NAME': 'HallwaySegmentCap',
        'IMG': 'images/hallwaysegmentcap.png',
        'REQS': []
    }

    HallwaySegmentCapWindow = {
        'NAME': 'HallwaySegmentCapWindow',
        'IMG': 'images/hallwaysegmentcapwindow.png',
        'REQS': []
    }
