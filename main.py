import pygame
import random

# 初期設定
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("横スクロールシューティングゲーム")

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# プレイヤー設定
player_size = 50
player_x, player_y = 50, screen_height // 2
player_speed = 5

# 弾丸設定
bullet_width, bullet_height = 10, 5
bullet_speed = 10
bullets = []

# 敵設定
enemy_width, enemy_height = 50, 50
enemy_speed = 3
enemies = []

# ゲームループの制御
clock = pygame.time.Clock()
running = True
score = 0

def draw_player(x, y):
	pygame.draw.rect(screen, BLUE, (x, y, player_size, player_size))

def draw_bullet(bullets):
	for bullet in bullets:
		pygame.draw.rect(screen, RED, (bullet[0], bullet[1], bullet_width, bullet_height))

def draw_enemy(enemies):
	for enemy in enemies:
		pygame.draw.rect(screen, WHITE, (enemy[0], enemy[1], enemy_width, enemy_height))

# ゲームループ
while running:
	screen.fill(BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				# 弾丸を発射
				bullets.append([player_x + player_size, player_y + player_size // 2 - bullet_height // 2])

	# プレイヤーの移動
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP] and player_y > 0:
		player_y -= player_speed
	if keys[pygame.K_DOWN] and player_y < screen_height - player_size:
		player_y += player_speed

	# 弾丸の移動
	for bullet in bullets:
		bullet[0] += bullet_speed
	bullets = [bullet for bullet in bullets if bullet[0] < screen_width]

	# 敵の出現と移動
	if random.randint(1, 20) == 1:
		enemies


def draw_bullet(bullets):
	for bullet in bullets:
		pygame.draw.rect(screen, RED, (bullet[0], bullet[1], bullet_width, bullet_height))

def draw_enemy(enemies):
	for enemy in enemies:
		pygame.draw.rect(screen, WHITE, (enemy[0], enemy[1], enemy_width, enemy_height))

def spawn_enemy():
	enemy_x = screen_width
	enemy_y = random.randint(0, screen_height - enemy_height)
	enemies.append([enemy_x, enemy_y])

def update_bullets():
	global score
	for bullet in bullets[:]:
		bullet[0] += bullet_speed
		if bullet[0] > screen_width:
			bullets.remove(bullet)
		else:
			# 弾と敵の衝突判定
			for enemy in enemies[:]:
				if (enemy[0] < bullet[0] < enemy[0] + enemy_width and
					enemy[1] < bullet[1] < enemy[1] + enemy_height):
					bullets.remove(bullet)
					enemies.remove(enemy)
					score += 1
					break

def update_enemies():
	for enemy in enemies[:]:
		enemy[0] -= enemy_speed
		if enemy[0] < 0:
			enemies.remove(enemy)

# メインゲームループ
spawn_counter = 0
while running:
	screen.fill(BLACK)

	#動作チェック
	print("Player Position:", player_x, player_y)
	print("Number of Bullets:", len(bullets))
	print("Number of Enemies:", len(enemies))


	# イベント処理
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bullet_x = player_x + player_size
				bullet_y = player_y + player_size // 2 - bullet_height // 2
				bullets.append([bullet_x, bullet_y])

	# プレイヤーの移動処理
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP] and player_y > 0:
		player_y -= player_speed
	if keys[pygame.K_DOWN] and player_y < screen_height - player_size:
		player_y += player_speed

	# 敵の生成
	spawn_counter += 1
	if spawn_counter > 30:  # 30フレームごとに敵を生成
		spawn_enemy()
		spawn_counter = 0

	# 弾丸と敵の更新
	update_bullets()
	update_enemies()

	# 描画
	draw_player(player_x, player_y)
	draw_bullet(bullets)
	draw_enemy(enemies)

	# スコアの描画
	font = pygame.font.Font(None, 36)
	score_text = font.render("Score: " + str(score), True, WHITE)
	screen.blit(score_text, (10, 10))

	pygame.display.flip()
	clock.tick(60)

pygame.quit()

