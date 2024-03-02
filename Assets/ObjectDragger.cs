using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObjectDragger : MonoBehaviour
{
    private Vector3 offset;

    private void OnMouseDown()
    {
        offset = transform.position - BuildingSystem.GetMouseWorldPosition() + offset;
    }

    private void OnMouseDrag()
    {
        Vector3 pos = BuildingSystem.GetMouseWorldPosition() + offset;
        transform.position = BuildingSystem.current.SnapCoordinateToGrid(pos);
    }
}
