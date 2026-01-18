using UnityEngine;

[RequireComponent(typeof(Rigidbody2D))]
public class PlayerController : MonoBehaviour
{
    public float moveSpeed = 6f;
    public float fireRate = 0.2f;
    public GameObject projectilePrefab;
    public Transform firePoint;
    public float projectileSpeed = 10f;

    Rigidbody2D rb;
    Vector2 input;
    float nextFireTime;

    void Awake()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        // Mobile: replace with Input System / joystick values
        input.x = Input.GetAxis("Horizontal");
        input.y = Input.GetAxis("Vertical");

        if (Input.GetButton("Fire1") || Input.GetMouseButton(0))
        {
            TryFire();
        }
    }

    void FixedUpdate()
    {
        rb.velocity = input.normalized * moveSpeed;
        // Keep player on-screen bounds (simple)
        Vector3 pos = Camera.main.WorldToViewportPoint(transform.position);
        pos.x = Mathf.Clamp01(pos.x);
        pos.y = Mathf.Clamp01(pos.y);
        transform.position = Camera.main.ViewportToWorldPoint(pos);
    }

    void TryFire()
    {
        if (Time.time >= nextFireTime && projectilePrefab != null && firePoint != null)
        {
            var proj = Instantiate(projectilePrefab, firePoint.position, Quaternion.identity);
            var rbp = proj.GetComponent<Rigidbody2D>();
            if (rbp) rbp.velocity = Vector2.up * projectileSpeed;
            nextFireTime = Time.time + fireRate;
        }
    }
}