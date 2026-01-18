using UnityEngine;

public class Enemy : MonoBehaviour
{
    public int health = 3;
    public float speed = 2f;
    public int scoreValue = 100;

    void Update()
    {
        transform.Translate(Vector2.down * speed * Time.deltaTime);
    }

    public void TakeDamage(int d)
    {
        health -= d;
        if (health <= 0) Die();
    }

    void Die()
    {
        if (GameManager.Instance != null) GameManager.Instance.AddScore(scoreValue);
        // TODO: spawn explosion VFX
        Destroy(gameObject);
    }
}