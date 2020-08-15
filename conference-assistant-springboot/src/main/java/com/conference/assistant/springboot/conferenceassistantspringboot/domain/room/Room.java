package com.conference.assistant.springboot.conferenceassistantspringboot.domain.room;

import com.conference.assistant.springboot.conferenceassistantspringboot.domain.BaseTimeEntity;
import com.conference.assistant.springboot.conferenceassistantspringboot.domain.team.Team;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.springframework.boot.autoconfigure.domain.EntityScan;

import javax.persistence.*;

@Getter
@NoArgsConstructor
@Entity
public class Room extends BaseTimeEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(nullable = false, name="room_id")
    private Long id;

    @Column(nullable = false, name="room_name")
    private String name;

    @Column(nullable = false, name="status_room")
    @Enumerated(EnumType.STRING)
    private Status status;

    // team id 참조
    @ManyToOne
    @JoinColumn(name="team_id")
    private Team team;

    @Builder
    public Room(String name, Status status, Team team) {
        this.name = name;
        this.status = status;
        this.team = team;
    }
}
