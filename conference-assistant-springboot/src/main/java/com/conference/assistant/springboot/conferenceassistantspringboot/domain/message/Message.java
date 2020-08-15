package com.conference.assistant.springboot.conferenceassistantspringboot.domain.message;

import com.conference.assistant.springboot.conferenceassistantspringboot.domain.BaseTimeEntity;
import com.conference.assistant.springboot.conferenceassistantspringboot.domain.room.Room;
import com.conference.assistant.springboot.conferenceassistantspringboot.domain.team.Team;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import javax.persistence.*;
import java.time.LocalDateTime;

@NoArgsConstructor
@Getter
@Entity
public class Message extends BaseTimeEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(nullable = false, name="message_id")
    private Long id;

    @Column(nullable = false)
    private String context;

    // room id 참조
    @ManyToOne
    @JoinColumn(name="room_id")
    private Room room;

    @Builder
    public Message(String context, Room room) {
        this.context = context;
        this.room = room;
    }
}
