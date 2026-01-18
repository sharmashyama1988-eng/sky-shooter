using UnityEngine;

public class Projectile : MonoBehaviour
{
    public float lifeSeconds = 5f;
    public int damage = 1;

    void Start()
    {
        Destroy(gameObject, lifeSeconds);
    }

    void OnTriggerEnter2D(Collider2D other)
    {
        var enemy = other.GetComponent<Enemy>();
        if (enemy != null)
        {
            enemy.TakeDamage(damage);
            Destroy(gameObject);
        }
    }
}